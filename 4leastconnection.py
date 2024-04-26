def create_server(name, weight):
    return {"name": name, "weight": weight, "current_weight": 0, "active_connections": 0}

def create_load_balancer(servers):
    return {"servers": servers, "last_selected": 0}

def add_server(load_balancer, server):
    load_balancer["servers"].append(server)

def get_least_connections_server(load_balancer):
    servers = load_balancer["servers"]
    min_connections = min(server["active_connections"] for server in servers)
    least_connections_servers = [server for server in servers if server["active_connections"] == min_connections]
    
    # Select the next server in the least_connections_servers list using a round-robin approach
    selected_server = least_connections_servers[load_balancer["last_selected"] % len(least_connections_servers)]
    selected_server["active_connections"] += 1
    load_balancer["last_selected"] += 1
    
    return selected_server

def release_connection(server):
    server["active_connections"] -= 1

def prompt_server_info(index):
    name = input(f"Enter the name of server {index}: ")
    weight = int(input(f"Enter the weight of server {index}: "))
    return create_server(name, weight)

def assign_load(load_balancer, i):
    next_server = get_least_connections_server(load_balancer)
    print(f"Load {i} assigned to server: {next_server['name']}")
    # Simulating the release of connection after processing the load
    release_connection(next_server)

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
