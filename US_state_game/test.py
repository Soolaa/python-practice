import pandas

data = pandas.read_csv("50_states.csv")

data_state = data[data.state == "Iowa"]
print(data_state.x)


print(type(data_state))
print(type(data_state.x))
print(type(data_state.x.item()))