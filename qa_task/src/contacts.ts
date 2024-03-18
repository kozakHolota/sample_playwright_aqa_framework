import localforage from "localforage";
import { matchSorter } from "match-sorter";
import sortBy from "sort-by";

export interface ContactEntry {
  id: string;
  first: string;
  last: string;
  avatar: string;
  twitter: string;
  notes: string;
  favorite: boolean;
  createdAt: number;
}

export async function getContacts(query?: string | null) {
  await fakeNetwork(`getContacts:${query}`);
  let contacts: Array<ContactEntry> = await localforage.getItem("contacts") as Array<ContactEntry>;
  if (!contacts) contacts = [];
  if (query) {
    contacts = matchSorter(contacts, query, { keys: ["first", "last"] });
  }
  return contacts.sort(sortBy("last", "createdAt"));
}

export async function createContact() {
  // @ts-expect-error it's a dummy
  await fakeNetwork();
  const id = Math.random().toString(36).substring(2, 9);
  const contact = { id, createdAt: Date.now() };
  const contacts = await getContacts() as Array<ContactEntry>;
  // @ts-expect-error it's a dummy
  contacts.unshift(contact);
  await set(contacts);
  return contact;
}

export async function getContact(id: string) {
  await fakeNetwork(`contact:${id}`);
  const contacts = await localforage.getItem("contacts") as Array<ContactEntry>;
  const contact = contacts.find(contact => contact.id === id);
  return contact ?? null;
}

export async function updateContact(id: string, updates: any) {
  // @ts-expect-error it's a dummy
  await fakeNetwork();
  const contacts = await localforage.getItem("contacts") as Array<ContactEntry>;
  const contact = contacts.find(contact => contact.id === id) as ContactEntry | null;
  if (!contact) throw new Error(`No contact found for ${id}`);
  Object.assign(contact, updates);
  await set(contacts);
  return contact;
}

export async function deleteContact(id) {
  const contacts = await localforage.getItem("contacts") as Array<ContactEntry>;
  const index = contacts.findIndex(contact => contact.id === id);
  if (index > -1) {
    contacts.splice(index, 1);
    await set(contacts);
    return true;
  }
  return false;
}

function set(contacts) {
  return localforage.setItem("contacts", contacts);
}

// fake a cache so we don't slow down stuff we've already seen
let fakeCache = {};

async function fakeNetwork(key) {
  if (!key) {
    fakeCache = {};
  }

  if (fakeCache[key]) {
    return;
  }

  fakeCache[key] = true;
  return new Promise(res => {
    setTimeout(res, Math.random() * 800);
  });
}
