'''
------------>  Advance min() and max() Functions<-------------
--------------------------------------------------------------
'''

def any_fun(name):
	return len(name)

names=["Apple","joy","om","ram kumar"]

print(max(names,key=any_fun))

print(max(names,key= lambda name: len(name)))

#1 find the name of highest marks:
student1 = [{"name":"Ram","score":60,"age":19},{"name":"kiran","score":70,"age":20},{"name":"om","score":80,"age":21}]

student2 = {"Ram":{"score":60,"age":19},"kiran":{"score":70,"age":20},"om":{"score":80,"age":21}}


