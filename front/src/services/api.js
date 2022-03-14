import config from "@/config.js";

export async function getRestaurants() {
  var response = await fetch(`${config.API_PATH}/restaurants`);
  const restaurants = await response.json();
  return restaurants;
}

export async function getListOfMenus() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: localStorage.id_restaurant,
    },
  };
  const response = await fetch(`${config.API_PATH}/menus`, settings);
  const listOfMenus = await response.json();
  return listOfMenus;
}

export async function getMenuByDate(date) {
  const settings = {
    method: "GET",
    headers: {
      Authorization: localStorage.id_restaurant,
    },
  };
  const response = await fetch(
    `${config.API_PATH}/menus/by-date/` + date,
    settings
  );
  const menus = await response.json();
  return menus;
}

export async function getMenuModify() {
  const settings = {
    method: "GET",
    headers: {
      Authorization: localStorage.id_restaurant,
    },
  };
  const response = await fetch(
    `${config.API_PATH}/menus/` + localStorage.id_menu,
    settings
  );
  const dict_plates = await response.json();
  return dict_plates;
}

export async function updateMenu(menu) {
  const settings = {
    method: "PUT",
    body: JSON.stringify(menu),
    headers: {
      Authorization: localStorage.id_restaurant,
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/menus`, settings);
}
