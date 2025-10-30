// リリィジュリッチ No.78 - 動的リダイレクトハンドラー
// デバッグモード: 開発者ツールのコンソールで動作確認可能

(function() {
  'use strict';

  // 派生URLと販売リンクの対応マッピング
  const redirectMap = {
    '/1': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q3pp22zj',
    '/2': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q33f45o4',
    '/3': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41qhnrzmng',
    '/4': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q1o5alqr',
    '/5': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6ud4gaywna',
    '/6': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q4mbpxi9',
    '/7': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo2rk9rpd',
    '/8': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo3bj5gfr',
    '/9': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo3sxn5jm',
    '/10': 'https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q28cb1ef'
  };

  // デフォルトリンク（パスが一致しない場合のフォールバック）
  const defaultUrl = 'https://www.wellbest.jp/Landing/Formlp/rereje_rich_drta_amgif_2503com_up_after.aspx';

  // 現在のURLパスを取得
  const currentPath = window.location.pathname;

  // デバッグログ: 現在のパスを出力
  console.log('=== リリィジュリッチ No.78 リダイレクトハンドラー ===');
  console.log('現在のパス:', currentPath);

  // パスに対応する販売リンクを取得
  const targetUrl = redirectMap[currentPath] || defaultUrl;

  // デバッグログ: 遷移先URLを出力
  console.log('遷移先URL:', targetUrl);
  console.log('対応マップ:', redirectMap);
  console.log('==============================================');

  // DOMContentLoaded後に全リンクを書き換え
  document.addEventListener('DOMContentLoaded', function() {
    // 全てのCTAリンク（data-ga-event属性を持つ要素）を取得
    const ctaLinks = document.querySelectorAll('[data-ga-event="cta_click"]');

    console.log(`CTAリンク数: ${ctaLinks.length}個を検出`);

    // 各CTAリンクのhref属性を動的に書き換え
    ctaLinks.forEach(function(link, index) {
      const originalHref = link.getAttribute('href');
      link.setAttribute('href', targetUrl);

      // デバッグログ: 書き換え結果を出力
      console.log(`[${index + 1}] CTAリンク書き換え完了`);
      console.log(`  元のURL: ${originalHref}`);
      console.log(`  新URL: ${targetUrl}`);
      console.log(`  GAラベル: ${link.getAttribute('data-ga-label')}`);
    });

    console.log('全てのCTAリンクの書き換えが完了しました。');
  });

  // 既存のGA処理とCTAクリックハンドラーは維持
  function sendGAEvent(eventName, params) {
    if (typeof gtag !== 'undefined') {
      gtag('event', eventName, params);
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    // CTAクリックイベントの処理
    document.querySelectorAll('[data-ga-event="cta_click"]').forEach(function(element) {
      element.addEventListener('click', function(event) {
        const label = element.getAttribute('data-ga-label') || 'default';

        // GAイベント送信
        sendGAEvent('cta_click', {
          event_category: 'engagement',
          event_label: label,
          value: 1
        });

        // デバッグログ: クリックイベント
        console.log('=== CTAクリック検出 ===');
        console.log('GAラベル:', label);
        console.log('遷移先:', element.href);
        console.log('====================');

        // 遷移を100ms遅延（GA送信を確実にするため）
        event.preventDefault();
        setTimeout(function() {
          window.location.href = element.href;
        }, 100);
      });
    });
  });

})();
