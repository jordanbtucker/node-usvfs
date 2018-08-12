const path = require('path')
const tap = require('tap')

const USVFS = require('..')

// Create a new instance of USVFS with a unique instance name.
const usvfs = new USVFS('node')

tap.test('Spawns notepad', async () => {
	// Only tests that it doesn't throw.

	// Clear all directory mappings.
	usvfs.clearMappings()

	// Recursively link a real directory to a virtual one.
	usvfs.linkDirectory(
		path.resolve(__dirname, 'fixtures/s'),
		path.resolve(__dirname, 'fixtures/d')
	)

	// Spawn a process that will see the virtual links.
	// Ensure that Notepad sees both `test/fixtures/s` and `test/fixtures/d`.
	usvfs.spawn('notepad.exe')
})
