# Aplicacion del servidor
from microdot import Microdot, send_file
from machine import Pin

app = Microdot()

led1

@app.route("<dir>/<file>")
async def static