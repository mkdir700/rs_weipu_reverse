var code = function () {
  var org = document.cookie.__lookupSetter__('cookie');
  document.__defineSetter__("cookie", function (cookie) {
    if (cookie.indexOf('GW1gelwM5YZuT') > -1) {
      var t = cookie.split("=")[1].split(";")[0];
      window.t_cookie = t;
      window.stop();
    } else if (cookie.indexOf('GW1gelwM5YZuS') > -1) {
      var s = cookie.split("=")[1].split(";")[0];
      window.s_cookie = s;
      console.log(s);
    }
    return org;
  });
  document.__defineGetter__("cookie", function () {
    // return document.cookie;
    return org;
  });
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head || document.documentElement).appendChild(script);
script.parentNode.removeChild(script);