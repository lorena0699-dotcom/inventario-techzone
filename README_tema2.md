# 📦 Sistema de Gestión de Inventario - TechZone S.R.L.

Aplicación web interactiva desarrollada con **Streamlit + Pandas** para gestionar el inventario de equipos informáticos de TechZone S.R.L.

## 🚀 Funcionalidades

- Carga automática del inventario desde `InventarioTechZone.xlsx`
- Filtros interactivos: por categoría, estado, rango de precios, nombre y stock crítico
- Registro de nuevos productos con validación de datos
- Cálculo automático de estado según stock (Disponible / Crítico / Agotado)
- Métricas avanzadas: Valor Total, Margen de Ganancia, Días en Inventario
- Gráficos: barras por categoría, circular por valor total, TOP 5 productos más valiosos

## 🛠️ Tecnologías

- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- OpenPyXL

## ⚙️ Instalación y uso local

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/inventario-techzone.git
cd inventario-techzone

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la aplicación
streamlit run ExamenT2.py
```

> ⚠️ Asegúrate de que el archivo `InventarioTechZone.xlsx` esté en la misma carpeta que `ExamenT2.py`.

## 📁 Estructura del proyecto

```
inventario-techzone/
├── ExamenT2.py
├── InventarioTechZone.xlsx
├── requirements.txt
└── README.md
```

## 👨‍💻 Desarrollado por

Tu Nombre Aquí  
Curso: Aplicaciones Interactivas para Análisis de Datos e Inteligencia Artificial  
Instituto INTECSSA
