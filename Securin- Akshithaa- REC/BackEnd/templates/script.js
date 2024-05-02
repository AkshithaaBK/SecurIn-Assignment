document.addEventListener('DOMContentLoaded', function() {
    fetch('/cves')
        .then(response => response.json())
        .then(data => {
            renderTable(data);
        })
        .catch(error => console.error('Error fetching data:', error));
   
    function renderTable(data) {
        const tableContainer = document.getElementById('table-container');
        const cves = data;

        const table = document.createElement('table');
        const headerRow = table.insertRow();
        const headers = ['CVE ID', 'Description', 'Published Date', 'Last Modified Date'];

        headers.forEach(header => {
            const th = document.createElement('th');
            th.textContent = header;
            headerRow.appendChild(th);
        });

        cves.forEach(cve => {
            const row = table.insertRow();
            const cells = [cve.cveID, cve.description, cve.publishedDate, cve.lastModifiedDate];

            cells.forEach(cellData => {
                const cell = document.createElement('td');
                cell.textContent = cellData;
                row.appendChild(cell);
            });
        });

        tableContainer.appendChild(table);
    }
});
