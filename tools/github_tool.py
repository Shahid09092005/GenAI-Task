import requests

def search_github(query, limit=3):
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "per_page": limit}

    r = requests.get(url, params=params)
    data = r.json()

    return [
        {
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        }
        for repo in data.get("items", [])
    ]
