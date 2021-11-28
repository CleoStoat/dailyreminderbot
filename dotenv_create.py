from config import credentials

def main():
    env_vars = {}
    for key in credentials:
        value = input(f"{key}=")
        value = value.strip()
        env_vars[key] = value

    env_vars_strings = [
        f"{key}={value}\n"
        for key, value in env_vars.items()
    ]

    with open(".env", mode="w") as f:
        f.writelines(env_vars_strings)
    

if __name__ == "__main__":
    main()