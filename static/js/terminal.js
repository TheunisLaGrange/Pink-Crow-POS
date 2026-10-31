let catalogMatrix = {};
let lastTransaction = null;
let activeCategoryFilter = "ALL"; // Tracks dynamic filtering state state

function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active-content'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    document.getElementById(tabId).classList.add('active-content');
    event.currentTarget.classList.add('active');
}

// Fetch dynamic configuration mapping down from server route on initialization
async function initializeCatalog() {
    try {
        const response = await fetch('/api/menu');
        catalogMatrix = await response.json();
        
        // Extract distinct categories from catalog mapping dynamically to keep it dictionary agnostic
        const categories = new Set(["ALL"]);
        Object.keys(catalogMatrix).forEach(name => {
            if (catalogMatrix[name].category) {
                categories.add(catalogMatrix[name].category);
            }
        });

        renderFilterButtons(Array.from(categories));
        renderCatalogViews();
    } catch (err) {
        console.error("Failed to map dynamic pipeline layout assets:", err);
    }
}

// Generate the Dynamic Category filter track pills
function renderFilterButtons(categoryList) {
    const filterBar = document.getElementById('category-filter-bar');
    filterBar.innerHTML = "";
    
    categoryList.forEach(cat => {
        const pill = document.createElement('button');
        pill.className = `filter-pill ${cat === activeCategoryFilter ? 'active-pill' : ''}`;
        pill.innerText = cat;
        pill.onclick = (e) => {
            document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active-pill'));
            e.currentTarget.classList.add('active-pill');
            activeCategoryFilter = cat;
            renderCatalogViews(); // Refresh view state grid items
        };
        filterBar.appendChild(pill);
    });
}

// Filters and Renders Card items inside layout grid
function renderCatalogViews() {
    const dropdown = document.getElementById('item_name');
    const gridContainer = document.getElementById('visual-menu-grid');
    
    dropdown.innerHTML = "";
    gridContainer.innerHTML = "";
    
    Object.keys(catalogMatrix).forEach(name => {
        const item = catalogMatrix[name];
        
        // 1. Core Dropdown Population
        const option = document.createElement('option');
        option.value = name;
        option.innerText = `${name} ($${item.price.toFixed(2)})`;
        dropdown.appendChild(option);
        
        // 2. Filter-Driven Card Generation
        if (activeCategoryFilter === "ALL" || item.category === activeCategoryFilter) {
            const card = document.createElement('div');
            card.className = "menu-card";
            card.onclick = () => selectCardItem(name);
            card.innerHTML = `
                <div class="card-icon">${item.icon}</div>
                <div class="card-title">${name}</div>
                <div class="card-price">$${item.price.toFixed(2)}</div>
            `;
            gridContainer.appendChild(card);
        }
    });
}

function selectCardItem(name) {
    document.getElementById('item_name').value = name;
    switchTab('checkout-tab');
}

// Run asset load hooks automatically
window.onload = initializeCatalog;
