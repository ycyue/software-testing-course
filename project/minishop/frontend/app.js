const loginForm = document.getElementById("login-form");
const shopPanel = document.getElementById("shop-panel");
const loginPanel = document.getElementById("login-panel");
const loginMsg = document.getElementById("login-msg");

function authHeaders() {
  const token = sessionStorage.getItem("minishop_token");
  return token ? { Authorization: "Bearer " + token, "Content-Type": "application/json" } : { "Content-Type": "application/json" };
}

const registerForm = document.getElementById("register-form");
const registerMsg = document.getElementById("register-msg");
if (registerForm) {
  registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const phone = document.getElementById("reg-phone").value;
    const password = document.getElementById("reg-password").value;
    const display_name = document.getElementById("reg-name").value;
    const res = await fetch("/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phone, password, display_name }),
    });
    const body = await res.json();
    if (res.status === 201) {
      registerMsg.textContent = "注册成功，请使用该手机号登录。未自动登录。";
    } else {
      registerMsg.textContent = "注册失败：" + (body.error || res.status);
    }
  });
}

loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const phone = document.getElementById("phone").value;
  const password = document.getElementById("password").value;
  const res = await fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone, password }),
  });
  const body = await res.json();
  if (res.status !== 200) {
    loginMsg.textContent = "登录失败";
    return;
  }
  sessionStorage.setItem("minishop_token", body.token);
  sessionStorage.setItem("minishop_role", body.role);
  loginMsg.textContent = "登录成功";
  loginPanel.hidden = true;
  const registerPanel = document.getElementById("register-panel");
  if (registerPanel) registerPanel.hidden = true;
  shopPanel.hidden = false;
  document.getElementById("who").textContent = phone + " (" + body.role + ")";
  await refreshProducts("");
  await refreshCart();
});

document.getElementById("search-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const keyword = document.getElementById("keyword").value;
  await refreshProducts(keyword);
});

async function refreshProducts(keyword) {
  const url = "/api/products" + (keyword !== undefined && keyword !== null ? "?keyword=" + encodeURIComponent(keyword) : "");
  const res = await fetch(url);
  const body = await res.json();
  const list = document.getElementById("product-list");
  const msg = document.getElementById("search-msg");
  list.innerHTML = (body.items || []).map(it => "<li>" + it.sku + " " + it.name + " 库存 " + it.stock + "</li>").join("");
  msg.textContent = "共 " + (body.items || []).length + " 件";
}

async function refreshCart() {
  const res = await fetch("/api/cart", { headers: authHeaders() });
  if (res.status !== 200) return;
  const body = await res.json();
  document.getElementById("cart-list").innerHTML =
    (body.items || []).map(it => "<li>" + it.sku + " qty=" + it.qty + " stock=" + it.stock + "</li>").join("");
}

document.getElementById("cart-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const sku = document.getElementById("cart-sku").value;
  const qty = Number(document.getElementById("cart-qty").value);
  const res = await fetch("/api/cart/items", {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ sku, qty }),
  });
  const body = await res.json();
  document.getElementById("cart-msg").textContent = res.status === 200 ? "已更新" : (body.error || "失败");
  await refreshCart();
});

document.getElementById("order-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const sku = document.getElementById("order-sku").value;
  const qty = Number(document.getElementById("order-qty").value);
  const res = await fetch("/api/orders", {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ sku, qty }),
  });
  const body = await res.json();
  if (res.status === 201) {
    document.getElementById("order-msg").textContent = "订单 id=" + body.id;
  } else {
    document.getElementById("order-msg").textContent = body.error || "下单失败";
  }
});
