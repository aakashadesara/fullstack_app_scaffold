const API_URL = "http://localhost:8000";

export const GET = (path, params = {}) => {
  const url = `${API_URL}${path}?` + new URLSearchParams(params);

  return fetch(url, {
    headers: {
      Accept: "application/json",
    },
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => {
      return new Promise((res, rej) => {
        res(data);
      });
    });
};

export const POST = (path, body = {}) => {
  return fetch(`${API_URL}${path}?`, {
    headers: {
      Accept: "application/json",
    },
    method: "post",
    body: JSON.stringify(body),
  }).then((res) => res.json());
};

export const DELETE = (path, body = {}) => {
  return fetch(`${API_URL}${path}?`, {
    headers: {
      Accept: "application/json",
    },
    method: "delete",
    body: JSON.stringify(body),
  }).then((res) => res.json());
};

export const PUT = (path, body = {}) => {
  return fetch(`${API_URL}${path}?`, {
    headers: {
      Accept: "application/json",
    },
    method: "put",
    body: JSON.stringify(body),
  }).then((res) => res.json());
};
