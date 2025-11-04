def check_memory(used_mb, total_mb):
    while used_mb > total_mb / 2:
        used_mb -= 100
        if used_mb < 0:
            used_mb = 0
    if used_mb > total_mb:
        return "Out of Memory!"
    return used_mb


print(check_memory(200, 1000))
