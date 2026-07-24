import React, { useState, useEffect } from "react";
import { ordersAPI } from "./api/ordersAPI";
import OrderCard from "./components/OrderCard";

export default function App() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    ordersAPI
      .getOrders()
      .then(setOrders)
      .catch((err) => console.error("Error loading orders:", err));
  }, []);

  const handleOrder = async () => {
    setLoading(true);
    try {
      const newOrder = await ordersAPI.createOrder(5);
      setOrders((prev) => [newOrder, ...prev]);
    } catch (err) {
      console.error("Error creating order:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "480px",
        margin: "40px auto",
        padding: "24px",
      }}
    >
      <header style={{ textAlign: "center", marginBottom: "32px" }}>
        <h1 style={{ margin: "0 0 8px 0", color: "#1f2937" }}>🍽️ Table #5</h1>
        <p style={{ margin: 0, color: "#6b7280", fontSize: "14px" }}>
          Professional Fullstack Architecture
        </p>
      </header>

      <button
        onClick={handleOrder}
        disabled={loading}
        style={{
          width: "100%",
          padding: "16px",
          fontSize: "16px",
          fontWeight: "600",
          color: "#ffffff",
          backgroundColor: loading ? "#9ca3af" : "#ef4444",
          border: "none",
          borderRadius: "12px",
          cursor: loading ? "not-allowed" : "pointer",
          boxShadow: "0 4px 12px rgba(239, 68, 68, 0.25)",
        }}
      >
        {loading ? "Sent to the kitchen..." : "🍳 Order the dish of the day"}
      </button>

      <section style={{ marginTop: "40px" }}>
        <h3 style={{ color: "#374151", marginBottom: "16px" }}>
          📋 Order History ({orders.length})
        </h3>
        <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
          {orders.map((order) => (
            <OrderCard key={order.id} order={order} />
          ))}
        </div>
      </section>
    </div>
  );
}
