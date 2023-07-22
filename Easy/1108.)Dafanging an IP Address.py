def defang_IP_addr(address: str):
    split_ip = address.split(".")
    result = "[.]".join(split_ip)
    return result


print(defang_IP_addr("1.1.1.1"))
print(defang_IP_addr("255.100.50.0"))