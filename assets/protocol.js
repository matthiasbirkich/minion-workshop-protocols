document.addEventListener("DOMContentLoaded", () => {
  const pageKey = window.location.pathname;

  document.querySelectorAll('.task-list input[type="checkbox"]').forEach((box, index) => {
    box.disabled = false;
    const key = `sharkseq:${pageKey}:task:${index}`;
    const saved = localStorage.getItem(key);
    if (saved !== null) box.checked = saved === '1';
    box.addEventListener('change', () => localStorage.setItem(key, box.checked ? '1' : '0'));
  });

  document.querySelectorAll('.protocol-notes').forEach((field) => {
    const key = `sharkseq:${pageKey}:note:${field.dataset.noteId}`;
    const saved = localStorage.getItem(key);
    if (saved !== null) field.value = saved;
    field.addEventListener('input', () => localStorage.setItem(key, field.value));
  });

  document.querySelectorAll('.protocol-input, .protocol-select').forEach((field) => {
    const id = field.dataset.fieldId;
    if (!id) return;
    const key = `sharkseq:${pageKey}:field:${id}`;
    const saved = localStorage.getItem(key);
    if (saved !== null) field.value = saved;
    field.addEventListener('input', () => localStorage.setItem(key, field.value));
    field.addEventListener('change', () => localStorage.setItem(key, field.value));
  });

  document.querySelectorAll('[data-reset-protocol]').forEach((button) => {
    button.addEventListener('click', () => {
      if (!confirm('Clear saved checkboxes, selections and notes for this page?')) return;
      Object.keys(localStorage).forEach((key) => {
        if (key.startsWith(`sharkseq:${pageKey}:`)) localStorage.removeItem(key);
      });
      window.location.reload();
    });
  });
});
