import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import uuid

st.title("Sistema de Gestión de Inventario - TechZone S.R.L.")


# Pregunta 1

try:
    df = pd.read_excel("InventarioTechZone.xlsx")
except FileNotFoundError:
    st.error("❌ El archivo InventarioTechZone.xlsx no fue encontrado.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error al cargar el archivo: {e}")
    st.stop()


# Pregunta 2
df["FechaIngreso"] = pd.to_datetime(df["FechaIngreso"])

st.subheader("Inventario Completo")
st.dataframe(df)


# Pregunta 9

def determinar_estado(stock):
    if stock == 0:
        return "Agotado"
    elif stock < 5:
        return "Crítico"
    else:
        return "Disponible"

df["Estado"] = df["Stock"].apply(determinar_estado)


# Pregunta 10

df["ValorTotal"] = df["Precio"] * df["Stock"]
df["MargenGanancia"] = round(df["Precio"] * 0.12, 2)
df["DiasEnInventario"] = (pd.Timestamp.today() - df["FechaIngreso"]).dt.days


# FILTROS 

st.subheader("Filtros")

# Pregunta 3 - Filtro por categoría
categorias = ["Laptop", "Monitor", "Accesorio", "Periférico", "Componente"]
categorias_sel = st.multiselect("Categoría:", categorias, default=categorias)

# Pregunta 4
estados = ["Disponible", "Agotado", "Descontinuado", "Crítico"]
estados_sel = st.multiselect("Estado:", estados, default=estados)

# Pregunta 5
precio_min = float(df["Precio"].min())
precio_max = float(df["Precio"].max())
rango_precio = st.slider("Rango de precios:", precio_min, precio_max, (precio_min, precio_max))

# Pregunta 6
busqueda = st.text_input("Buscar producto por nombre o palabra clave:")

# Pregunta 7
filtrar_stock = st.checkbox("Mostrar solo productos con stock crítico (< 5)")


df_filtrado = df[df["Categoria"].isin(categorias_sel)]
df_filtrado = df_filtrado[df_filtrado["Estado"].isin(estados_sel)]
df_filtrado = df_filtrado[(df_filtrado["Precio"] >= rango_precio[0]) & (df_filtrado["Precio"] <= rango_precio[1])]

if busqueda:
    df_filtrado = df_filtrado[df_filtrado["Producto"].str.contains(busqueda, case=False, na=False)]

if filtrar_stock:
    df_filtrado = df_filtrado[df_filtrado["Stock"] < 5]

st.subheader("Inventario Filtrado con Métricas")
st.dataframe(df_filtrado)


# Pregunta 8

def generar_codigo():
    return str(uuid.uuid4())[:8].upper()

st.subheader("Registrar Nuevo Producto")

nombre = st.text_input("Nombre del producto")
categoria_form = st.selectbox("Categoría", ["Laptop", "Monitor", "Accesorio", "Periférico", "Componente"])
precio_form = st.number_input("Precio unitario", min_value=0.0, step=0.01)
stock_form = st.number_input("Stock disponible", min_value=0, step=1)
fecha_ingreso_form = st.date_input("Fecha de ingreso")

if st.button("Registrar producto"):
    errores = []
    if not nombre:
        errores.append("El nombre no puede estar vacío.")
    if precio_form <= 0:
        errores.append("El precio debe ser mayor que 0.")
    if stock_form < 0:
        errores.append("El stock no puede ser negativo.")
    if fecha_ingreso_form > date.today():
        errores.append("La fecha no puede ser futura.")

    if errores:
        for e in errores:
            st.error(e)
    else:
        codigo = generar_codigo()
        st.success(f"✅ Producto '{nombre}' registrado con código: {codigo}")


# Pregunta 11

st.subheader("Gráficos")

# Barras + Circular juntos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

conteo_cat = df_filtrado["Categoria"].value_counts()
ax1.bar(conteo_cat.index, conteo_cat.values)
ax1.set_title("Cantidad de productos por categoría")
ax1.set_xlabel("Categoría")
ax1.set_ylabel("Cantidad")
ax1.tick_params(axis="x", rotation=45)

valor_cat = df_filtrado.groupby("Categoria")["ValorTotal"].sum()
ax2.pie(valor_cat, labels=valor_cat.index, autopct="%1.1f%%")
ax2.set_title("Valor total por categoría")

plt.tight_layout()
st.pyplot(fig)

# TOP 5
st.subheader("TOP 5 Productos más valiosos")
top5 = df_filtrado.nlargest(5, "ValorTotal")
fig2, ax3 = plt.subplots(figsize=(8, 4))
ax3.barh(top5["Producto"], top5["ValorTotal"])
ax3.set_title("TOP 5 Productos por Valor Total")
ax3.set_xlabel("Valor Total")
plt.tight_layout()
st.pyplot(fig2)