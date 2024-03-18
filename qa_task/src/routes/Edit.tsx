import { Form, redirect, useLoaderData, useNavigate } from "react-router-dom";
import { ContactEntry, updateContact } from "../contacts";

export async function editAction({ request, params }) {
  const formData = await request.formData();
  const updates = Object.fromEntries(formData);
  await updateContact(params.contactId, updates);
  return redirect(`/contacts/${params.contactId}`);
}

export default function EditContact() {
  const { contact } = useLoaderData() as { contact: ContactEntry };
  const navigate = useNavigate();

  return (
    <Form method="post" id="contact-form">
      <p>
        <span>Name</span>
        <input
          placeholder="First"
          aria-label="First name"
          type="text"
          name="first"
          defaultValue={contact.first}
          data-testid="first"
        />
        <input
          placeholder="Last"
          aria-label="Last name"
          type="text"
          name="last"
          defaultValue={contact.last}
          data-testid="last"
        />
      </p>
      <label>
        <span>Twitter</span>
        <input
          type="text"
          name="twitter"
          placeholder="@jack"
          defaultValue={contact.twitter}
          data-testid="twitter"
        />
      </label>
      <label>
        <span>Avatar URL</span>
        <input
          placeholder="https://example.com/avatar.jpg"
          aria-label="Avatar URL"
          type="text"
          name="avatar"
          defaultValue={contact.avatar}
          data-testid="avatar"
        />
      </label>
      <label>
        <span>Notes</span>
        <textarea
          name="notes"
          defaultValue={contact.notes}
          rows={6}
          data-testid="notes"
        />
      </label>
      <p>
        <button type="submit" data-testid="save-contact">
          Save
        </button>
        <button
          type="button"
          onClick={() => {
            navigate(-1);
          }}
          data-testid="cancel-contact"
        >
          Cancel
        </button>
      </p>
    </Form>
  );
}
