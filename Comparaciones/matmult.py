import numpy as np 
import time
import csv

N=np.array([10,20,30,50,100,200,500,1000,1200,1500,2000])

t=[]
N_rep=5;


f=open('tiemposmatmultPY.csv','w')
wr=csv.writer(f,delimiter=',')
wr.writerow(["# N elementos procesados", "Tiempo Promedio[ms]", "STD Tiempo [ms]", " #100 rep"])


for i in N:

	for j in range(0,N_rep):
		matrizA=np.random.randint(2e8-1,size=(i,i))
		matrizB=np.random.randint(2e8-1,size=(i,i))

		inicio = time.time()
		matrizC=np.dot(matrizA,matrizB)
		fin = time.time()
		t.append(fin-inicio)



	temp=np.array(t)*1000
	tmp_ms=temp.mean()
	var=np.sqrt(temp.var()/(N_rep-1))
	wr.writerow(np.array([round(i),round(tmp_ms,5),round(var,5)]))

f.close()
