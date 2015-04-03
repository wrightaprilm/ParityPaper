all : model_fits  

model_fits: ./Trees/Time-Scaled/*.dated ./Scripts/bisse.r
	R CMD BATCH ./Scripts/bisse.r 
	


