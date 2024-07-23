import time
source = "reportLine += 1"
reportLine=0

start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled=stop-start

#compile - prekompilacja kodu (co, plik gdy brak to jakiś tekst, exex/eval/single (metoda))
sourceCompiled = compile(source, 'internal variable source', 'exec')

start = time.time()
for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
time_compiled=stop-start

print(time_not_compiled)
print(time_compiled)
print(time_not_compiled/time_compiled)

