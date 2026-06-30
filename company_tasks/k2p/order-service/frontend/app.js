const API = "http://127.0.0.1:8000";

function log(data) {
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}

async function request(path, options) {
  const res = await fetch(`${API}${path}`, options);
  const data = await res.json();

  if (!res.ok) {
    log({ error: data.detail || "Request failed" });
    return null;
  }

  log(data);
  return data;
}

async function createClient() {
  const name = document.getElementById("clientName").value.trim();

  await request("/clients/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name })
  });
}

async function createProduct() {
  const name = document.getElementById("productName").value.trim();
  const price = parseFloat(document.getElementById("productPrice").value);

  await request("/products/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name, price })
  });
}

async function createOrder() {
  const client_id = parseInt(document.getElementById("orderClientId").value);
  const productId1 = parseInt(document.getElementById("orderProductId1").value);
  const quantity1 = parseInt(document.getElementById("orderQuantity1").value);
  const productId2 = parseInt(document.getElementById("orderProductId2").value);
  const quantity2 = parseInt(document.getElementById("orderQuantity2").value);

  const items = [
    { product_id: productId1, quantity: quantity1 }
  ];

  if (!Number.isNaN(productId2)) {
    items.push({ product_id: productId2, quantity: quantity2 });
  }

  await request("/orders/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ client_id, items })
  });
}
