#!/usr/bin/env bash
# Exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate --no-input

# Recolectar archivos estáticos
python manage.py collectstatic --no-input
