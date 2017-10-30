num = 0
for v in range(1,10):
	for r in range(1,10):
		for s in range(1,10):
			for w in range(0,10):
				for z in range(0,10):
					d=set([v,r,s,w,z])
					if ((v*100+w*10+w+r*1000+w*100+z*10+w-(s*1000+s*100+w*10+s)==0) and (len(d)==5)):
						num+=1
print(num)
