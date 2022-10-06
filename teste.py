from minizinc import Instance, Model, Solver
import pandas as pd

# Create a MiniZinc model
model = Model()
model.add_string("""
set of int: A;
set of int: B;
var A : x;
var B : y;
constraint x+y >= 3;
constraint x!=y;
solve satisfy;
""")

# Transform Model into a instance
gecode = Solver.lookup("gecode")
inst = Instance(gecode, model)

# Entrada de Dados
inst['A'] = range(0, 4)
inst['B'] = range(0, 4)

# Solve the instance
result = inst.solve(all_solutions=True)
# print(result)

# for i in range(len(result)):
#     print("x_{} = {} and y_{} = {}".format(i, result[i, "x"], i, result[i, "y"]))

# Agrega os valores em um data frame para análise
solution = pd.DataFrame({'x': [result[i, 'x'] for i in range(len(result))], 'y': [result[i, 'y'] for i in range(len(result))]})

#Consistencias

if not solution.query('x==y').empty:
    print('Problema - Soluções não podem ser iguais')

# data = pd.read_excel('Book1.xlsx')
# grouped = data.drop(['d', 'h'], axis = 1).groupby(['dh'], axis = 0).count().rename(columns = {'dis':'qtde'})
#apirest postman

