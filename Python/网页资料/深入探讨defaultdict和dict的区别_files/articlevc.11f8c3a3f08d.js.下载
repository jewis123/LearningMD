window.addEventListener('DOMContentLoaded', function () {
  class VisitCounter {
    constructor() {
      try {
        this.visitsForDay = JSON.parse(localStorage.getItem("rpvc"));
      } catch {
        this.visitsForDay = {}
      }
      if (this.visitsForDay === null) {
        this.visitsForDay = {}
      }
    }

    persist() {
      localStorage.setItem("rpvc", JSON.stringify(this.visitsForDay));
    }

    countToday() {
      let isoToday = (new Date()).toISOString().slice(0, 10);
      if (!this.visitsForDay.hasOwnProperty(isoToday)) {
        this.visitsForDay[isoToday] = 0;
      }
      this.visitsForDay[isoToday] = this.visitsForDay[isoToday] + 1;
    }

    prune(cutoffDays) {
      var cutoff = new Date()
      cutoff.setDate(cutoff.getDate() - cutoffDays);

      var newVisitsForDay = {};

      for (var isoDay in this.visitsForDay) {
        var day = new Date(isoDay);
        if (day >= cutoff) {
          newVisitsForDay[isoDay] = this.visitsForDay[isoDay];
        }
      }

      this.visitsForDay = newVisitsForDay;
    }

    visits() {
      var total = 0;
      for (var isoDay in this.visitsForDay) {
        total += this.visitsForDay[isoDay];
      }
      return total;
    }

    markNotified() {
      let now = new Date();
      localStorage.setItem("rp-lastnotified", now.toISOString());
    }

    lastNotified() {
      return new Date(localStorage.getItem("rp-lastnotified"));
    }

    daysSinceLastNotified() {
      let seconds = (new Date()) - this.lastNotified()
      return Math.floor(seconds / (1000 * 60 * 60 * 24));
    }
  }

  function hideElem(className) {
    let results = document.getElementsByClassName(className);
    if (results.length === 0) {
      setTimeout(() => hideElem(className), 100);
      return;
    }
    Array.from(results).forEach((el) => {
      el.hidden = true;
    });
  }

  let counter = new VisitCounter();
  counter.countToday();
  counter.prune(30);
  counter.persist();

  let visits = counter.visits();
  if (visits > 10) {
    ga('send', {
      hitType: 'event',
      eventCategory: 'rpvc',
      eventAction: 'wouldshow',
      eventValue: visits
    });

    if (counter.daysSinceLastNotified() >= 7) {
      counter.markNotified();
      $("#rpvc").modal({ backdrop: 'static', keyboard: false });

      hideElem("addthis-smartlayers");
      hideElem("drip-tab-container");

      ga('send', {
        hitType: 'event',
        eventCategory: 'rpvc',
        eventAction: 'didshow',
        eventValue: visits
      });
    }
  }
});
