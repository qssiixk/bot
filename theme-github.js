define("ace/theme/github",["require","exports","module","ace/lib/dom"], function(require, exports, module) {

    var dom = require("../lib/dom");
    dom.importCssString(exports.cssText, exports.cssClass, false);
});                (function() {
                    window.require(["ace/theme/github"], function(m) {
                        if (typeof module == "object" && typeof exports == "object" && module) {
                            module.exports = m;
                        }
                    });
                })();
