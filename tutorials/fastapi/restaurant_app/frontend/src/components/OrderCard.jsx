import React from 'react';

export default function OrderCard({ order }) {
  return (
    <div
      style={{
        border: "1px solid #e0e0e0",
        borderRadius: "10px",
        padding: "14px 18px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        backgroundColor: "#ffffff",
        boxShadow: "0 2px 4px rgba(0,0,0,0.04)",
      }}
    >
      <div>
        <span style={{ color: "#888888", fontSize: "14px" }}>
          Order #{order.id} (Table #{order.table_number})
        </span>
        <div style={{ fontWeight: "600", fontSize: "16px", marginTop: "4px" }}>
          {order.dish_name}
        </div>
      </div>
      <span
        style={{
          color: "#10b981",
          backgroundColor: "#ecfdf5",
          padding: "6px 12px",
          borderRadius: "20px",
          fontSize: "13px",
          fontWeight: "500",
        }}
      >
        {order.status}
      </span>
    </div>
  );
}