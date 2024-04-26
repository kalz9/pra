def create_server(name, weight):
    return {"name": name, "weight": weight, "current_weight": 0, "active_connections": 0}

def create_load_balancer(servers):
    return {"servers": servers, "current_server_index": 0}

def add_server(load_balancer, server):
    load_balancer["servers"].append(server)

def get_next_server(load_balancer):
    current_server_index = load_balancer["current_server_index"]
    next_server_index = (current_server_index + 1) % len(load_balancer["servers"])
    load_balancer["current_server_index"] = next_server_index
    return load_balancer["servers"][next_server_index]

def assign_load(load_balancer, i):
    next_server = get_next_server(load_balancer)
    print(f"Load {i} assigned to server: {next_server['name']}")
    next_server["active_connections"] += 1

def release_connection(server):
    server["active_connections"] -= 1

def prompt_server_info(index):
    name = input(f"Enter the name of server {index}: ")
    weight = int(input(f"Enter the weight of server {index}: "))
    return create_server(name, weight)

if __name__ == "__main__":
    servers = []
    num_servers = int(input("Enter the number of servers: "))
    for i in range(1, num_servers + 1):
        servers.append(prompt_server_info(i))

    lb = create_load_balancer(servers)

    num_loads = int(input("Enter the number of loads: "))

    print("\nLoad balancing result:")
    for i in range(1, num_loads + 1):
        assign_load(lb, i)
