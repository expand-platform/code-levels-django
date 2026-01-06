import { saveToLocalStorage, loadFromLocalStorage } from "./../../helpers/localStorage.js";

const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

const sidebarStateKey = 'isDashboardSidebarHidden';

menuBar.addEventListener('click', function () {
    sidebar.classList.toggle('hide');
    let isSidebarHidden = sidebar.classList.contains('hide');
    console.log("🚀 ~ isSidebarHidden (after click):", isSidebarHidden)

    saveToLocalStorage(sidebarStateKey, isSidebarHidden);
});

export function loadSidebarState() {
    let isSidebarHidden = loadFromLocalStorage(sidebarStateKey);

    /* ! after page loaded, class is added, animation is toggled (bad) */

    if (isSidebarHidden) {
        sidebar.classList.add('hide');
    } else {
        console.log('- else -');
        
        sidebar.classList.remove('hide');
    }

    console.log('- sidebar is set to:', isSidebarHidden);
    
}

function adjustSidebar() {
    if (window.innerWidth <= 576) {
        sidebar.classList.add('hide');
        // sidebar.classList.remove('show');
    } else {
        sidebar.classList.remove('hide');
        // sidebar.classList.add('show');
    }
}

// Sayfa yüklendiğinde ve pencere boyutu değiştiğinde sidebar durumunu ayarlama
// window.addEventListener('load', adjustSidebar);
window.addEventListener('resize', adjustSidebar);