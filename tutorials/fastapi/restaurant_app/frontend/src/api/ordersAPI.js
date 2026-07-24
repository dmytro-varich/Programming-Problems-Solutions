import { apiRequest } from "./client";

export const ordersAPI = {
  getOrders: () => apiRequest("/orders"),
  createOrder: (tableNumber = 5) =>
    apiRequest("/orders", {
      method: "POST",
      body: JSON.stringify({ table_number: tableNumber }),
    }),
};
