import eel
import mainscript as m

eel.init("templates")
eel.start("index.html", block=False, size=(600, 600))

@eel.expose
def run(path):
    print(path)
    r = m.segragete(path)
    eel.result(r)

while True:
    eel.sleep(10)