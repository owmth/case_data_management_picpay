def test_create_user_duplicate_email():
    client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    response = client.post("/users/", json={"name": "Another", "email": "john@example.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "E-mail já cadastrado!"

def test_get_non_existing_user():
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"

def test_update_user_duplicate_email():
    client.post("/users/", json={"name": "User1", "email": "user1@example.com"})
    user2 = client.post("/users/", json={"name": "User2", "email": "user2@example.com"}).json()
    
    response = client.put(f"/users/{user2['id']}", json={"name": "Updated", "email": "user1@example.com"})
    assert response.status_code == 400
    assert response.json()["detail"] == "E-mail já cadastrado!"
