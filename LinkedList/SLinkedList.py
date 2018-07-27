class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class SLinked_List:
	def __init__(self):
		self.head=None
		self.size=0
	def append(self,item):
		temp=ListNode(item)
		if self.head == None:
			self.head=temp
		else:
			current=self.head
			while current.next != None:
				current=current.next
			current.next=temp
		self.size+=1

	def add_elements(self,elements):
		for i in elements:
			self.append(i)

	def search(self,item):
		
		current=self.head

		while current != None:
			if current.val == item:
				return current
			current=current.next

	def reverse(self):
		previous=None
		current=self.head
		while current is not None:
			next_node=current.next
			current.next=previous
			previous=current
			current=next_node
		self.head=previous
			
	def __str__(self):
		output = []
		current = self.head
		while current:
			output.append(current.val)
			current = current.next
		output=[str(i) for i in output]
		return "->".join(output) 
