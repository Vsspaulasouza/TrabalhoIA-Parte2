const barraDeTexto = document.querySelector("#entrada");
const telaDeMensagens = document.querySelector(".principal");
const formulario = document.querySelector("form");

function getCookie(name) {
  let cookie = document.cookie.match("(^|;) ?" + name + "=([^;]*)(;|$)");
  return cookie ? cookie[2] : null;
}

function scroll(elemento) {
  telaDeMensagens.scrollTo({
    top: elemento.offsetTop,
    behavior: "smooth",
  });
}

function mostraMensagem(texto, classes, html = null) {
  let mensagem = document.createElement("p");
  mensagem.innerHTML = html;
  if (!html) mensagem.innerText = texto;
  mensagem.classList.add("msg", ...classes);
  telaDeMensagens.appendChild(mensagem);
  scroll(mensagem);
  return mensagem;
}

function permiteEnvio(opcao) {
  if (!opcao) {
    barraDeTexto.disabled = true;
    formulario.removeEventListener("submit", leMensagemUsuario);
    formulario.addEventListener("submit", (event) => event.preventDefault());
    return;
  }
  barraDeTexto.disabled = false;
  formulario.removeEventListener("submit", (event) => event.preventDefault());
  formulario.addEventListener("submit", leMensagemUsuario);
}

async function carregandoResposta(mensagem) {
  let html =
    '<span class="ponto"></span><span class="ponto ponto2"></span><span class="ponto ponto3"></span>';
  let esperando = mostraMensagem(" ", ["msgBot", "esperando"], html);
  barraDeTexto.value = "";

  permiteEnvio(false);

  let url = "/enviaMsg";
  let dados = new FormData();
  dados.append("entrada", mensagem);
  let options = {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: dados,
  };

  await fetch(url, options)
    .then((response) => response.json())
    .then((json) => json.resposta)
    .then((resposta) => (esperando.innerHTML = resposta))
    .catch((error) => {
      console.log(error);
      esperando.innerHTML = "Desculpe, ocorreu um erro :(";
    })
    .finally(() => {
      scroll(esperando);
      permiteEnvio(true);
    });
}

function leMensagemUsuario(event) {
  event.preventDefault();
  if (barraDeTexto.value) {
    mostraMensagem(barraDeTexto.value, ["msgUser"]);
    carregandoResposta(barraDeTexto.value);
  }
}

formulario.addEventListener("submit", leMensagemUsuario);
