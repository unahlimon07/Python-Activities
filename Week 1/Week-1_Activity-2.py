


# Calculate the total commission earned by Agent, unit manager, branch head in 5 years-
# -if client pays 100,000 per year

# Year 1	(Selling agent 25%, Unit Manager 15%, Branch Head 10%)	
# Year 2	(Selling agent 8%, Unit Manager 5%, Branch Head 2%)	
# Year 3	(Selling agent 5%, Unit Manager 4%, Branch Head 1%)	
# Year 4	(Selling agent 3%, Unit Manager 2%, Branch Head 0%)	
# Year 5	(Selling agent 2%, Unit Manager 1% Branch Head 0%)	

# no if else involve in this problem

print('-----------------[ 5 year Insurance Commission Calculation]------------------')

client_payment = 100000
agent_total_commission = 0
manager_total_commission = 0
head_total_commission = 0

# Year 1
agent_total_commission += client_payment*0.25
manager_total_commission += client_payment*0.15
head_total_commission += client_payment*0.10

# Year 2
agent_total_commission += client_payment*0.08
manager_total_commission += client_payment*0.05
head_total_commission += client_payment*0.02

# Year 3
agent_total_commission += client_payment*0.05
manager_total_commission += client_payment*0.04
head_total_commission += client_payment*0.01

# Year 4
agent_total_commission += client_payment*0.03
manager_total_commission += client_payment*0.02

# Year 5
agent_total_commission += client_payment*0.02
manager_total_commission += client_payment*0.01

print("5 years commission breakdown: ")
print(f'Agent: {agent_total_commission}')
print(f'Unit manager: {manager_total_commission}')
print(f'Branch Head: {head_total_commission}')


# TEST CASE:
# 5 years commission breakdown:
# Agent: 43000.0
# Unit manager: 27000.0
# Branch Head: 13000.0