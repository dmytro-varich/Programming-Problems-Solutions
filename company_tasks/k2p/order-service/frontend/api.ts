const API = "http://127.0.0.1:8000";

type Client = {
  id: number;
  name: string;
};

export async function createClient(name: string): Promise<Client> {
  const res = await fetch(`${API}/clients/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  });

  return res.json();
}