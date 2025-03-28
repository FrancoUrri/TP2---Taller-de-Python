def time_reaction_category():
	time_reaction = int(input("Ingre su tiempo de reacción en ms: "))
	classif_list = ["Lento", "Normal", "Rápido"]
	if time_reaction < 200:
		return classif_list[2]
	elif time_reaction > 500:
		return classif_list[0]
	else:
		return classif_list[1]