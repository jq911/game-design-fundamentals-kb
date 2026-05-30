(() => {
  const protectedPrefix = '/game-design-fundamentals/';
  const sitePath = window.location.pathname;
  if (!sitePath.includes(protectedPrefix)) return;

  const storageKey = 'gdf_kb_unlocked_v1';
  // Default local password: azu
  // To change it, run scripts/hash_password.py and replace this hash.
  const passwordHash = '5b4356878451530cb5a8224af7bb5aa1e9316e73dc77942649ebbfe78d4e4196';

  const encoder = new TextEncoder();
  async function sha256(text) {
    const buffer = await crypto.subtle.digest('SHA-256', encoder.encode(text));
    return [...new Uint8Array(buffer)].map((b) => b.toString(16).padStart(2, '0')).join('');
  }

  function unlock(options = {}) {
    document.documentElement.classList.remove('book-locked');
    document.documentElement.classList.add('book-unlocked');
    const gate = document.querySelector('.book-gate');
    if (gate) gate.remove();
    if (options.reload) {
      window.location.reload();
    }
  }

  function mountGate() {
    document.documentElement.classList.add('book-locked');
    const gate = document.createElement('div');
    gate.className = 'book-gate';
    gate.innerHTML = `
      <form class="book-gate__panel" autocomplete="off">
        <div class="book-gate__eyebrow">PRIVATE READING VAULT</div>
        <h1>请输入访问密码</h1>
        <p>《游戏设计基础（原书第3版）》包含本地私人整理内容。解锁后仅在本机浏览器保存访问状态。</p>
        <label class="book-gate__field">
          <span>密码</span>
          <input type="password" name="password" autofocus required />
        </label>
        <button type="submit">进入书籍</button>
        <div class="book-gate__error" role="alert" aria-live="polite"></div>
      </form>
    `;
    document.body.appendChild(gate);

    const form = gate.querySelector('form');
    const input = gate.querySelector('input');
    const error = gate.querySelector('.book-gate__error');
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      const value = input.value.trim();
      if (!value) return;
      if (await sha256(value) === passwordHash) {
        sessionStorage.setItem(storageKey, '1');
        unlock({ reload: true });
      } else {
        error.textContent = '密码不正确，请重试。';
        input.select();
      }
    });
  }

  if (sessionStorage.getItem(storageKey) === '1') {
    unlock();
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountGate);
    } else {
      mountGate();
    }
  }
})();
