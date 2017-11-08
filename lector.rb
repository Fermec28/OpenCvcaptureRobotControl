def load_tasks (archivo)
  value=[]
   return value unless File::exists?(archivo) 
  keys=[:id,:name,:done]
  File.open(archivo).map do |line|
  p line.split(',')[2]
     {id: line.split(',')[0].to_i,
	name: line.split(',')[1],
	done: line.split(',')[2]== "true\n"}
  end  
end
p load_tasks("archivo.txt")

def save_tasks (arr) 
  #target=File.open(archivo, 'w')
  arr.each do |element|
	print element.values.join(",")
	print "\n"
  end    
end

save_tasks(load_tasks("archivo.txt"))