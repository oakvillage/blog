class AppHeader extends HTMLElement {
    connectedCallback() {
        this.textContent = 'Header.'
    }
}

customElements.define('AppHeader', AppHeader);