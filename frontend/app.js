async function loadTodos() {
  const res = await fetch("/todos");
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach(t => {
    const li = document.createElement("li");
    li.innerHTML = `${t.task} <button onclick="deleteTodo(${t.id})">X</button>`;
    list.appendChild(li);
  });
}

async function addTodo() {
  const task = document.getElementById("task").value;

  await fetch("/todos", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({task})
  });

  loadTodos();
}

async function deleteTodo(id) {
  await fetch(`/todos/${id}`, {method: "DELETE"});
  loadTodos();
}

window.onload = loadTodos;