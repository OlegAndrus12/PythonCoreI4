def url_builder(base_url):

    def with_params(path, **params):
        query = "&".join(f"{k}={v}" for k, v in params.items())
        return f"{base_url}{path}?{query}" if query else f"{base_url}{path}"

    
    return with_params


api = url_builder("https://api.company.com")

print(api("/users", page=1, limit=20))
print(api("/orders", status="pending", page=2))
print(api("/products"))
