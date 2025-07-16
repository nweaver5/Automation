import { test, expect } from '@playwright/test';

test('Verifying Dashboard Test', async({ page }) => {
  const start = 'https://tenonworkshop.service-now.com/navpage.do'
  await page.goto(start);
  await page.frameLocator('iframe[name="gsft_main"]').getByLabel('User name').fill('test.automate');
  await page.frameLocator('iframe[name="gsft_main"]').getByLabel('Password', { exact: true }).fill('Ten0nAutomat1on!');
  await page.frameLocator('iframe[name="gsft_main"]').getByRole('button', { name: 'Log in' }).click();
  await page.getByPlaceholder('Filter navigator').fill('Tenon Work');
  const tenonPagePromise = page.waitForEvent("popup");
  await page.getByRole('link', { name: 'Tenon Work', exact: true }).click();
  const tenonPage = await tenonPagePromise;

  await tenonPage.getByRole('heading', { name: 'Dashboard' });

  

  await tenonPage.pause();
});
