import numpy as np 
import time
import csv
import numexpr as ne 

ne.set_num_threads(8) 

N=np.array([1.00000000e+05, 1.43844989e+05, 2.06913808e+05, 2.97635144e+05,
       4.28133240e+05, 6.15848211e+05, 8.85866790e+05, 1.27427499e+06,
       1.83298071e+06, 2.63665090e+06, 3.79269019e+06, 5.45559478e+06,
       7.84759970e+06, 1.12883789e+07, 1.62377674e+07, 2.33572147e+07,
       3.35981829e+07, 4.83293024e+07, 6.95192796e+07, 1.00000000e+08],dtype=float)
N=np.around(N,0)

t=[]
t1=[]
N_rep=10;


f=open('tiemposNPYdotprod.csv','w',newline="")
wr=csv.writer(f,delimiter=',')
wr.writerow(["# N elementos procesados", "Tiempo Promedio[ms]", "STD Tiempo [ms]", " #100 rep"])

f1=open('tiemposNUMERdotprod_mcore.csv','w',newline="")
wr1=csv.writer(f1,delimiter=',')
wr1.writerow(["# N elementos procesados", "Tiempo Promedio[ms]", "STD Tiempo [ms]", " #100 rep"])



#Creamos el vector con los N elementos
for i in N:
 	for j in range(0,N_rep):
 		vectorA=np.random.rand(int(i))
 		vectorB=np.random.rand(int(i))

 		inicio = time.time_ns()
 		vectorC=np.dot(vectorA,vectorB)
 		fin = time.time_ns()
 		t.append(fin-inicio)

 		vectorA1=np.random.rand(int(i))
 		vectorB1=np.random.rand(int(i))
 		
 

 		inicio1 = time.time_ns()
 		aux = ne.evaluate('vectorA1*vectorB1')
 		aux1 = ne.evaluate('sum(aux)')
 		fin1 = time.time_ns()

 		t1.append(fin1-inicio1)


 	temp=np.array(t)/1000000
 	tmp_ms=temp.mean()
 	var=np.sqrt(temp.var()/(N_rep-1))
 	wr.writerow(np.array([round(i),round(tmp_ms,5),round(var,5)]))

 	temp1=np.array(t1)/1000000
 	tmp1_ms=temp1.mean()
 	var1=np.sqrt(temp1.var()/(N_rep-1))
 	wr1.writerow(np.array([round(i),round(tmp1_ms,5),round(var1,5)]))

f.close()
f1.close()