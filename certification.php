<?php
// certification.php - public page to list candidates and certifications
// Requires a db.php file with PDO $pdo and helper h() function
require_once __DIR__ . '/db.php';

// GET params
$q = isset($_GET['q']) ? trim($_GET['q']) : '';
$certFilter = isset($_GET['cert']) ? trim($_GET['cert']) : '';

// Prepare query for distinct certification names (for filter select)
$stmt = $pdo->query("SELECT DISTINCT name FROM certifications ORDER BY name");
$certNames = $stmt->fetchAll(PDO::FETCH_COLUMN);

// Build main query: fetch candidates and their certifications
$sql = "SELECT
    cand.id AS candidate_id,
    cand.first_name,
    cand.last_name,
    cand.email,
    cand.location,
    cert.id AS cert_id,
    cert.name AS cert_name,
    cert.issuer AS cert_issuer,
    cert.date_awarded AS cert_date_awarded,
    cert.expiration_date AS cert_expiration_date
  FROM candidates cand
  LEFT JOIN certifications cert ON cert.candidate_id = cand.id
  WHERE 1=1
";

$params = [];

if ($q !== '') {
    $sql .= " AND (
      CONCAT(cand.first_name, ' ', cand.last_name) LIKE :q
      OR cand.first_name LIKE :q
      OR cand.last_name LIKE :q
      OR cert.name LIKE :q
    )";
    $params[':q'] = "%$q%";
}

if ($certFilter !== '') {
    $sql .= " AND cert.name = :certFilter";
    $params[':certFilter'] = $certFilter;
}

$sql .= " ORDER BY cand.last_name, cand.first_name, cert.date_awarded DESC";

$stmt = $pdo->prepare($sql);
$stmt->execute($params);
$rows = $stmt->fetchAll();

// Group rows by candidate
$candidates = [];
foreach ($rows as $r) {
    $cid = $r['candidate_id'];
    if (!isset($candidates[$cid])) {
        $candidates[$cid] = [
            'id' => $cid,
            'first_name' => $r['first_name'],
            'last_name' => $r['last_name'],
            'email' => $r['email'],
            'location' => $r['location'],
            'certifications' => []
        ];
    }
    if ($r['cert_id']) {
        $candidates[$cid]['certifications'][] = [
            'id' => $r['cert_id'],
            'name' => $r['cert_name'],
            'issuer' => $r['cert_issuer'],
            'date_awarded' => $r['cert_date_awarded'],
            'expiration_date' => $r['cert_expiration_date']
        ];
    }
}
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Candidate Certifications</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <header class="header">
      <h1>Candidate Certifications</h1>

      <div class="controls">
        <form id="searchForm" method="get" class="search-box" aria-label="Search certifications">
          <input type="search" name="q" id="q" placeholder="Search by candidate or certification..." value="<?php echo h($q); ?>" />
          <select name="cert" id="cert">
            <option value="">All certifications</option>
            <?php foreach ($certNames as $name): ?>
              <option value="<?php echo h($name); ?>" <?php if ($name === $certFilter) echo 'selected'; ?>><?php echo h($name); ?></option>
            <?php endforeach; ?>
          </select>
          <button type="submit">Search</button>
        </form>
      </div>
    </header>

    <?php if (empty($candidates)): ?>
      <div class="card empty">
        No results. Try a different search or remove filters.
      </div>
    <?php else: ?>
      <section class="grid" aria-live="polite">
        <?php foreach ($candidates as $cand): ?>
          <article class="card" id="cand-<?php echo h($cand['id']); ?>">
            <h2><?php echo h($cand['first_name'] . ' ' . $cand['last_name']); ?></h2>
            <div class="meta">
              <?php if ($cand['location']): ?><div class="small"><?php echo h($cand['location']); ?></div><?php endif; ?>
              <?php if ($cand['email']): ?><div class="small"><?php echo h($cand['email']); ?></div><?php endif; ?>
            </div>

            <div class="cert-list" aria-label="Certifications">
              <?php if (empty($cand['certifications'])): ?>
                <div class="small">No certifications recorded.</div>
              <?php else: ?>
                <?php foreach ($cand['certifications'] as $cert): ?>
                  <div class="cert" title="<?php echo h($cert['issuer']); ?>">
                    <div style="flex:1;">
                      <?php echo h($cert['name']); ?>
                      <div class="small" style="font-weight:400"><?php echo h($cert['issuer']); ?></div>
                    </div>
                    <div style="margin-left:10px;text-align:right;">
                      <div class="small"><?php echo $cert['date_awarded'] ? h(date('Y-m-d', strtotime($cert['date_awarded']))) : ''; ?></div>
                      <?php if ($cert['expiration_date']): ?>
                        <div class="small">exp <?php echo h(date('Y-m-d', strtotime($cert['expiration_date']))); ?></div>
                      <?php endif; ?>
                    </div>
                  </div>
                <?php endforeach; ?>
              <?php endif; ?>
            </div>
          </article>
        <?php endforeach; ?>
      </section>
    <?php endif; ?>
  </div>
  <script src="certification.js" defer></script>
</body>
</html>
