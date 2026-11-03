<?php
declare(strict_types=1);

// Read-only diagnostic for the invoking CLI interpreter. Not an exploit or scanner.
if (PHP_SAPI !== 'cli') {
    http_response_code(403);
    exit("CLI-only diagnostic. No web request processing is supported.\n");
}

$result = [
    'scope' => 'invoking_cli_interpreter_only',
    'php_version' => PHP_VERSION,
    'sapi' => PHP_SAPI,
    'session_extension_loaded' => extension_loaded('session'),
    'session_upload_progress_enabled' => ini_get('session.upload_progress.enabled'),
    'session_serializer' => ini_get('session.serialize_handler'),
    'fatal_error_backtraces' => ini_get('fatal_error_backtraces'),
    'assessment' => 'NO_VULNERABILITY_OR_PATCH_VERDICT',
    'limitations' => [
        'Web workers may use a different interpreter or configuration.',
        'Runtime application overrides are not inspected.',
        'No requests are sent, no application is loaded, and no settings are changed.',
    ],
];
echo json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR), PHP_EOL;
