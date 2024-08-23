const hamburger = document.getElementById('hamburger');
const menu = document.querySelector('.menu');

hamburger.addEventListener('click', function () {
    const hamIcon = this.querySelector('.hamburger-icon');
    const crossIcon = this.querySelector('.cross-icon');
    if (hamIcon.style.display === "none") {
        hamIcon.style.display = "inline-block"
        menu.style.display = "none"
        crossIcon.style.display = "none"
    }
    else {
        crossIcon.style.display = "inline-block"
        hamIcon.style.display = "none"
        menu.style.display = "block"
    }
});
// Load the Google Charts library
google.charts.load('current', { 'packages': ['corechart'] });

// Set a callback to run when the Google Charts library is loaded
google.charts.setOnLoadCallback(drawTChart);
google.charts.setOnLoadCallback(drawSChart);

function drawTChart() {
  // Set Data
  const data = google.visualization.arrayToDataTable([
    ['Skill', 'Value'],
    ['HTML', 54.8],
    ['CSS', 48.6],
    ['Python', 44.4],
    ['Prompt Engineering', 23.9],
    ['JavaScript', 14.5]
  ]);

  // Set Options
  const options = {
    title: 'Technical Skills',
    backgroundColor: 'transparent',
    pieSliceTextStyle: {
      color: '#fff' // Change the color of the text inside pie slices
    },
    legend: {
      textStyle: {
        color: '#fff' // Change legend font color
      }
    },
    titleTextStyle: {
      color: '#fff', // Change title font color
      fontSize: 20 // Change title font size
    }
  };

  // Draw
  const chart = new google.visualization.PieChart(document.getElementById('technical'));
  chart.draw(data, options);
}

function drawSChart() {
  // Set Data
  const data = google.visualization.arrayToDataTable([
    ['Skill', 'Value'],
    ['Communication', 60.8],
    ['Collaborative', 45.6],
    ['Professionalism', 40.4],
    ['problem Solving', 17.9],
    ['Emotional Intelligence', 24.5]
  ]);

  // Set Options
  const options = {
    title: 'Soft Skills',
    backgroundColor: 'transparent',
    pieSliceTextStyle: {
      color: '#fff' // Change the color of the text inside pie slices
    },
    legend: {
      textStyle: {
        color: '#fff' // Change legend font color
      }
    },
    titleTextStyle: {
      color: '#fff', // Change title font color
      fontSize: 20 // Change title font size
    }
  };

  // Draw
  const chart = new google.visualization.PieChart(document.getElementById('soft'));
  chart.draw(data, options);
}

const anchorLinks = document.querySelectorAll('a[href*="#"]');

anchorLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const offset = link.getAttribute('data-offset');
    const target = document.querySelector(link.getAttribute('href'));
    const top = target.offsetTop - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});
