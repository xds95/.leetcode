import sys
import re 

if __name__ == '__main__':
	# sample = sys.stdin.readline().strip()
	sample = "The furthest distance in the world, Is not between life and death, But when I stand in front of you, Yet you don't know that I love you."
	# pre = sys.stdin.readline()
	pre = r'f'
	sample1 = [_ for _ in re.split(' |,|\'|\.',sample) if _]
	sample2 = sorted(set(sample1))
	re = [_ for _ in sample2 if pre == _[:len(pre)]]
	re = " ".join(re)
	print(sample1,sample2,re)