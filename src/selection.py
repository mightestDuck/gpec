from random import random
from src.utilities import normalize_vector, accumulate_vector


def roulette_wheel(quantity, scores):
	# Probability of being selected depends on the fitness
	indexes = []
	for _ in range(quantity):
		R = random()
		anl = accumulate_vector(normalize_vector(scores))
		for index, entry in enumerate(anl):
			if entry >= R:
				indexes.append(index)
	return indexes


def rank_based(quantity, population_size):
	# Probability of being selected depends on position in the rank
	indexes = []
	for _ in range(quantity):
		R = random()
		anl = accumulate_vector(normalize_vector([x for x in range(population_size, 0, -1)]))
		for index, entry in enumerate(anl):
			if entry >= R:
				indexes.append(index)
	return indexes


def truncation(quantity):
	return [i for i in range(quantity)]


def tournament():
	print('tobedone')


def sort_by_scores(scores):
	tmp_scores = scores
	scores = []
	while len(tmp_scores) > 0:
		best_score = 0
		best_score_index = 0
		for index, score in enumerate(tmp_scores):
			if score[1] > best_score:
				best_score = score[1]
				best_score_index = index
		scores.append(tmp_scores[best_score_index])
		tmp_scores.remove(tmp_scores[best_score_index])
	return scores